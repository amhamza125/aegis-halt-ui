# { "Depends": "py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng" }

import genlayer as gl
from genlayer.types import *


class TargetVault(gl.contract.Contract):

    aegis_guardian: Address
    is_paused: bool

    def __init__(
        self,
        aegis_address: str,
    ):
        self.aegis_guardian = Address(
            aegis_address
        )

        self.is_paused = False

    # ==================================================
    # EMERGENCY PAUSE
    # ==================================================

    @gl.public.write
    def emergency_pause(self) -> None:

        if gl.message.sender_address != self.aegis_guardian:
            raise gl.vm.UserError(
                "Unauthorized: Only Aegis can pause."
            )

        self.is_paused = True

    # ==================================================
    # STATUS
    # ==================================================

    @gl.public.view
    def get_status(self) -> str:

        if self.is_paused:
            return "PAUSED"

        return "ACTIVE"

    # ==================================================
    # GUARDIAN
    # ==================================================

    @gl.public.view
    def get_guardian(self) -> str:

        return str(self.aegis_guardian)