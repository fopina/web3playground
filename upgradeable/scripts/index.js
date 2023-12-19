// scripts/index.js
async function main () {
    // Set up an ethers contract, representing our deployed Box instance
    const address = '0x5FbDB2315678afecb367f032d93F642f64180aa3';
    const Box = await ethers.getContractFactory('Box');
    const box = await Box.attach(address);
    const value = await box.retrieve();
    console.log('Box value is', value.toString());
    await box.store(23);

    // Call the retrieve() function of the deployed Box contract
    const newValue = await box.retrieve();
    console.log('Box value is', newValue.toString());
  }
  
  main()
    .then(() => process.exit(0))
    .catch(error => {
      console.error(error);
      process.exit(1);
    });