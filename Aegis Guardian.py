# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *
from dataclasses import dataclass
import json
from datetime import datetime

@allow_storage
@dataclass
class ProtocolRecord:
    target_address: Address
    protocol_name: str
    is_halted: bool
    halt_reason: str
    last_trigger_time: bigint

class AegisHalt(gl.Contract):
    """
    Production-grade Autonomous Emergency Halt Module. 
    Monitors external DeFi protocols and automatically pauses them 
    via asynchronous internal messages after AI consensus.
    """
    owner: Address
    monitored_protocols: TreeMap[Address, ProtocolRecord]
    halt_events: TreeMap[bigint, str]
    event_count: bigint
    cooldown_seconds: bigint

    def __init__(self):
        self.owner = gl.message.sender_address
        self.event_count = bigint(0)
        self.cooldown_seconds = bigint(300)

    def _get_current_time(self) -> bigint:
        raw_dt = gl.message_raw.get("datetime", "")
        if not raw_dt:
            return bigint(0)
        clean_dt = raw_dt.replace("Z", "+00:00")
        try:
            dt = datetime.fromisoformat(clean_dt)
            return bigint(int(dt.timestamp()))
        except (ValueError, TypeError):
            return bigint(0)

    @gl.public.write
    def register_protocol(self, target_address: str, protocol_name: str) -> None:
        if gl.message.sender_address != self.owner:
            raise gl.vm.UserError("Unauthorized.")
        if not protocol_name.strip():
            raise gl.vm.UserError("Protocol name cannot be empty.")
        
        addr = Address(target_address)
        self.monitored_protocols[addr] = ProtocolRecord(
            target_address=addr,
            protocol_name=protocol_name.strip(),
            is_halted=False,
            halt_reason="",
            last_trigger_time=bigint(0)
        )

    @gl.public.write
    def trigger_halt(self, target_address: str, evidence_text: str) -> None:
        if not evidence_text.strip():
            raise gl.vm.UserError("Evidence text cannot be empty.")

        addr = Address(target_address)
        protocol = self.monitored_protocols[addr]
        
        if protocol.is_halted:
            raise gl.vm.UserError("Protocol is already halted.")

        current_time = self._get_current_time()

        def verify_exploit() -> str:
            prompt = f"""
            You are an elite Web3 security auditor AI.
            Analyze the following text.
            Determine if this text provides credible, explicit evidence of an ACTIVE EXPLOIT, 
            HACK, or CRITICAL VULNERABILITY currently draining or threatening the protocol named '{protocol.protocol_name}'.

            EVIDENCE TEXT:
            {evidence_text}

            INSTRUCTIONS:
            If the text proves an active hack/exploit, answer TRUE.
            If the text is unrelated or a generic warning, answer FALSE.
            Respond ONLY with the single word TRUE or FALSE. Do not include any other text.
            """
            result = gl.nondet.exec_prompt(prompt).strip().upper()
            return result if result in ("TRUE", "FALSE") else "FALSE"

        # Trigger AI Consensus Mechanism
        agreed_verdict = gl.eq_principle.prompt_comparative(
            verify_exploit,
            principle="Validators must reach unanimous consensus. Output must be exactly 'TRUE' or 'FALSE'."
        )
        
        protocol.last_trigger_time = current_time

        if agreed_verdict == "TRUE":
            deterministic_reason = "Exploit confirmed via on-chain AI text evaluation."
            
            # The Asynchronous Cross-Contract Call (Triggers upon 'accepted' state)
            target_contract = gl.get_contract_at(addr)
            target_contract.emit(on='accepted').emergency_pause()
            
            protocol.is_halted = True
            protocol.halt_reason = deterministic_reason
            
            self.halt_events[self.event_count] = f"ProtocolHalted: {protocol.protocol_name} at {target_address}. Reason: {deterministic_reason}"
            self.event_count += 1
            
        self.monitored_protocols[addr] = protocol

    @gl.public.view
    def get_protocol_status(self, target_address: str) -> str:
        addr = Address(target_address)
        if addr not in self.monitored_protocols:
            return "NOT_REGISTERED"
        protocol = self.monitored_protocols[addr]
        return json.dumps({
            "protocol_name": protocol.protocol_name,
            "status": "HALTED" if protocol.is_halted else "ACTIVE",
            "reason": protocol.halt_reason,
            "last_trigger": str(protocol.last_trigger_time)
        })

    @gl.public.view
    def get_halt_events(self) -> str:
        events_list = []
        count = int(self.event_count)
        for i in range(count):
            events_list.append({
                "event_id": i,
                "details": self.halt_events[bigint(i)]
            })
        return json.dumps(events_list, indent=2)
