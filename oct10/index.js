// ==========================================
// Part 1: Four helper functions
// ==========================================

function getBalance() {
  var balanceElement = document.getElementById("balance");
  return Number(balanceElement.innerText);
}

function setBalance(newBalance) {
  var balanceElement = document.getElementById("balance");
  balanceElement.innerText = newBalance;
}

function getAmount() {
  var amountElement = document.getElementById("amount");
  return Number(amountElement.value);
}

function setAmount(value) {
  var amountElement = document.getElementById("amount");
  amountElement.value = value;
}

// ==========================================
// Part 2 & Part 4: Credit Functionality
// ==========================================
var creditButton = document.getElementById("credit-btn");

creditButton.addEventListener("click", function () {
  var currentBalance = getBalance();
  var amount = getAmount();

  // Part 4: Refuse empty amount, 0, or negative numbers
  if (isNaN(amount) || amount <= 0) {
    alert("Please enter a valid amount greater than 0.");
    return;
  }

  var newBalance = currentBalance + amount;
  setBalance(newBalance);
  setAmount("");
});

// ==========================================
// Part 3, Part 4 & Part 5: Debit Functionality
// ==========================================
var debitButton = document.getElementById("debit-btn");

debitButton.addEventListener("click", function () {
  var currentBalance = getBalance();
  var amount = getAmount();

  // Part 4: Refuse empty amount, 0, or negative numbers
  if (isNaN(amount) || amount <= 0) {
    alert("Please enter a valid amount greater than 0.");
  } 
  // Part 5: Refuse a debit larger than the balance
  else if (amount > currentBalance) {
    alert("Insufficient funds! You cannot withdraw more than your balance.");
  } 
  else {
    var newBalance = currentBalance - amount;
    setBalance(newBalance);
    setAmount("");
  }
});