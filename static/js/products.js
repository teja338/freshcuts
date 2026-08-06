// ===============================
// Product Quantity Controls
// ===============================

// ===============================
// Product Quantity Controls
// ===============================

function increaseQty() {

    const quantity = document.getElementById("quantity");

    if (!quantity) return;

    quantity.value = parseInt(quantity.value) + 1;
}

function decreaseQty() {

    const quantity = document.getElementById("quantity");

    if (!quantity) return;

    let value = parseInt(quantity.value);

    if (value > 1) {
        quantity.value = value - 1;
    }
}

// ===============================
// Page Ready
// ===============================

document.addEventListener("DOMContentLoaded", function () {

    const quantity = document.getElementById("quantity");

    if (quantity) {
        quantity.value = 1;
    }

});
// ===============================
// Page Ready
// ===============================

document.addEventListener("DOMContentLoaded", function () {

    const quantity = document.getElementById("quantity");

    if (quantity) {
        quantity.value = 1;
    }

});
