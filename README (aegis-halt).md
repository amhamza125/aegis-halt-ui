# Aegis Guardian 🛡️ 

**An Autonomous Emergency Halt Module powered by GenLayer AI Consensus.**

Aegis Guardian actively monitors external DeFi protocols and automatically pauses them via asynchronous cross-contract messages when GenLayer's on-chain AI consensus detects a critical vulnerability, active exploit, or fund-draining attack.

🚀 **Live UI Simulation:** [https://aegis-halt-ui.vercel.app/](https://aegis-halt-ui.vercel.app/)

## 🌐 GenLayer Studio Next Deployments (Chain 61997)
The smart contracts are fully source-verified and actively deployed on the GenLayer Studio Next network:
* **Aegis Guardian:** [`0xD5414C390d50c58ef103404d88278cD8D0AB0E0F`](https://explorer-studio-dev.genlayer.com/address/0xD5414C390d50c58ef103404d88278cD8D0AB0E0F)
* **Target Vault:** [`0x6E7516F7E3E617552A91eD1E87Dc0E57090b5Bcf`](https://explorer-studio-dev.genlayer.com/address/0x6E7516F7E3E617552A91eD1E87Dc0E57090b5Bcf)

## 🏗️ Technical Architecture (v0.3.0 RC2 Compliant)
This project has been completely refactored to align with the GenVM v0.3.0 architecture requirements:
* **Strict Typing:** Utilizes standard Python `int` implementations (replacing legacy `u256`) for seamless database schema extraction and compilation.
* **Verified Dependencies:** Implements the official `9b8kjyda2ycxyq4ea6g4yfpnydxhd52gqba5rb8dw7krkh5mn9p0` runner hash for native execution on Chain 61997.
* **AI Consensus Protocol:** Integrates `gl.eq_principle.prompt_comparative` to force strict, unanimous AI evaluation of unstructured threat intelligence before triggering asynchronous cross-contract state changes.

## 💻 Frontend UI & Sandbox Mode
Due to RPC limitations on the beta testnet, a comprehensive Next.js web application was built to interact with the protocol via a **Sandbox Simulation**. 

The UI allows users to visually demonstrate the AI Guardian's internal threat detection, view the evaluation logs in real-time, and observe the resulting execution sequence that securely locks the Target Vault.

### Local Setup Instructions
To run the Next.js frontend locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/amhamza125/aegis-halt-ui.git](https://github.com/amhamza125/aegis-halt-ui.git)
   cd aegis-halt-ui
