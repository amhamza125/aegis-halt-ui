# 🛡️ AegisHalt Protocol

**Autonomous Emergency Halt Module built for the GenLayer Network.**

## Overview
AegisHalt is a decentralized AI Guardian for DeFi protocols. Instead of relying on slow human multisigs to pause a protocol during a hack, AegisHalt uses GenLayer's AI Validator network to read exploit evidence, achieve unanimous consensus, and automatically trigger a cross-contract pause.

## 🎥 Live Demo & Contracts
* **Video Demo:** [Watch the AegisHalt Execution](https://youtube.com/shorts/BqY8YH3lMlc?si=6lqSwrF-AFaw0Ulb)
* **Aegis Guardian (AI Oracle):** `0x97DDDa1A857d54c09E4E3007CE4f60C0a20BFF17`
* **DummyDeFiVault (Target):** `0xE32FD7A138171254659AbcdF92633A95DDaAdBa0`

## Architecture & Tech Stack
This project leverages a strict, professional 2-contract architecture to separate the Oracle logic from the Vault state.

* **GenLayer Python SDK & GenVM:** For deploying intelligent smart contracts.
* **Equivalence Principle (`gl.eq_principle.prompt_comparative`):** Enforces strict AI consensus. Validators must unanimously agree that the provided evidence constitutes a legitimate hack before any state changes occur.
* **Asynchronous Cross-Contract Execution (`emit(on='accepted')`):** Aegis utilizes GenLayer's internal messaging to asynchronously dispatch the `emergency_pause` execution to the target Vault immediately upon Oracle consensus.
