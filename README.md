# 🚀 Land Registry Blockchain

A **Blockchain-based Land Registry System** using **Ethereum**, **Solidity**, and **Web3.py** to ensure **secure, transparent, and immutable** land ownership records.

---

## 📌 Features
- 🏡 **Decentralized Land Registration**
- 🔗 **Ownership Transfer with Smart Contracts**
- 🔍 **Secure & Transparent Verification**
- ⚡ **Fast & Immutable Transactions**
- 🎯 **Web3 Integration with Python (Flask/Streamlit)**

---

## 🏗 Project Structure
```
📂 hiteshydv001-land-register-blockchain/
├── README.md                    # Project Documentation
├── package.json                  # Node.js dependencies (Truffle, Web3)
├── truffle-config.js             # Truffle Configuration
├── truffle-config-sepholia.js    # Truffle config for Sepolia Testnet
├── .env.local                    # Environment Variables
├── contracts/                     
│   ├── LandRegistry.sol          # Smart Contract
│   └── .gitkeep                  # Placeholder
├── migrations/                    
│   ├── 2_deploy_contracts.js     # Contract Deployment Script
│   └── .gitkeep                  # Placeholder
└── src/                          
    ├── app.py                    # Web Frontend (Flask/Streamlit)
    └── backend.py                 # Backend Integration with Web3
```

---

## 🚀 Getting Started
### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Node.js & npm** (For Truffle & Web3.js)
- **Python 3.8+** (For backend integration)
- **Ganache** (For local Ethereum blockchain)
- **MetaMask** (For interacting with contracts)

### 2️⃣ Installation
#### 🔹 Clone the Repository
```bash
git clone https://github.com/hiteshydv001/land-register-blockchain.git
cd land-register-blockchain
```
#### 🔹 Install Dependencies
```bash
npm install  # Install Truffle & Web3.js dependencies
python -m venv venv && source venv/bin/activate  # Create & activate Python virtual environment
pip install -r requirements.txt  # Install Python dependencies
```
#### 🔹 Start Ganache (for local development)
```bash
ganache-cli --port 7545
```
#### 🔹 Compile & Deploy Smart Contract
```bash
truffle compile
truffle migrate --network development
```
#### 🔹 Run Backend API
```bash
python src/backend.py
```
#### 🔹 Start Web Application (Optional)
```bash
python src/app.py  # If using Flask/Streamlit frontend
```

---

## 📜 Smart Contract Overview
### 🔹 LandRegistry.sol
- `registerLand(uint256 _id, string memory _location, uint256 _area)` → **Registers a new land**
- `transferOwnership(uint256 _id, address _newOwner)` → **Transfers land ownership**
- `getLand(uint256 _id)` → **Fetches land details**
- `isLandRegistered(uint256 _id)` → **Checks if land is registered**

---

## 🌍 Deploy on Ethereum Testnet (Sepolia)
1. **Update `truffle-config-sepholia.js` with Infura & Wallet Private Key**
2. **Deploy using Truffle**
```bash
truffle migrate --network sepolia
```
3. **Verify Smart Contract (Etherscan)**
```bash
truffle run verify LandRegistry --network sepolia
```

---

## ⚡ API Endpoints
| Method  | Endpoint                 | Description             |
|---------|--------------------------|-------------------------|
| `POST`  | `/register`              | Register a new land    |
| `POST`  | `/transfer`              | Transfer ownership     |
| `GET`   | `/get_land?land_id=1001` | Fetch land details     |
| `GET`   | `/is_registered?land_id=1001` | Check land registration |

---

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes (`git commit -m 'Added new feature'`)
4. Push to your branch (`git push origin feature-xyz`)
5. Submit a Pull Request 🚀

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ✨ Author
👤 **Hitesh Kumar**  
📧 [Email](mailto:hiteshofficial0001@gamil.com)  
🔗 [GitHub](https://github.com/Hiteshydv001) | [LinkedIn](https://www.linkedin.com/in/hitesh-kumar-aiml/)


