Land Registry Blockchain
A decentralized land registry system using Ethereum smart contracts, Truffle, Web3.py, and a Python-based backend.
Table of Contents
1. Features
2. Tech Stack
3. Installation
4. Usage
5. Directory Structure
6. Contributing
7. License
Features
- Decentralized land registration
- Smart contract-based ownership transfer
- Web3 integration with Python
- Secure and tamper-proof land records
Tech Stack
- **Blockchain:** Ethereum, Solidity, Ganache
- **Frameworks & Tools:** Truffle, Web3.py
- **Backend:** Python, Flask
- **Smart Contracts Deployment:** Truffle
Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hiteshydv001/land-register-blockchain.git
   ```
2. Install dependencies:
   ```bash
   cd land-register-blockchain
   npm install
   ```
3. Start Ganache and deploy smart contracts:
   ```bash
   truffle migrate --reset
   ```
4. Run the backend:
   ```bash
   python src/backend.py
   ```
Usage
Register land:
   ```python
   register_land(account, land_id, location, area)
   ```
Transfer ownership:
   ```python
   transfer_ownership(account, land_id, new_owner)
   ```
Check registration status:
   ```python
   is_land_registered(land_id)
   ```
Directory Structure
```
└── hiteshydv001-land-register-blockchain/
    ├── README.md
    ├── package.json
    ├── truffle-config-sepholia.js
    ├── truffle-config.js
    ├── .env.local
    ├── contracts/
    │   ├── LandRegistry.sol
    │   └── .gitkeep
    ├── migrations/
    │   ├── 2_deploy_contracts.js
    │   └── .gitkeep
    └── src/
        ├── app.py
        └── backend.py
```
Contributing
Feel free to fork this project, submit issues, or open pull requests.
License
This project is licensed under the MIT License.
