require("dotenv").config();
const HDWalletProvider = require("@truffle/hdwallet-provider");

const PRIVATE_KEY = process.env.PRIVATE_KEY;
const ALCHEMY_API_URL_SEPOLIA = process.env.ALCHEMY_API_URL_SEPOLIA;

module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",
      port: 7545,
      network_id: "*",
    },
    sepolia: {
      provider: () => new HDWalletProvider(PRIVATE_KEY, ALCHEMY_API_URL_SEPOLIA),
      network_id: 11155111,  // Sepolia network ID
      confirmations: 2,
      timeoutBlocks: 200,
      gas: 5000000,
      gasPrice: 30000000000,
      skipDryRun: true,
    },
  },
  mocha: {},
  compilers: {
    solc: {
      version: "0.8.20", // Use the latest Solidity version
    },
  },
};
