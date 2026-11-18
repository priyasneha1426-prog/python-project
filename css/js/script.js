
// Filter packages by region

function filterPackages() {
    const category = document.getElementById("category").value;
    const packages = document.querySelectorAll(".package-card");

    packages.forEach(function(item) {
        if (category === "all" || item.dataset.category === category) {
            item.style.display = "block";
        } else {
            item.style.display = "none";
        }
    });
}


// Calculate package cost

function calculateCost() {
    const price = Number(document.getElementById("selectedPackage").value);
    const people = Number(document.getElementById("people").value);

    if (!Number.isInteger(people) || people < 1 || people > 20) {
        alert("Please enter between 1 and 20 travellers.");
        return;
    }

    const total = price * people;

    document.getElementById("totalCost").textContent =
        "Estimated Total: ₹" + total.toLocaleString("en-IN");
}


// Select package for enquiry

function bookPackage(name, price) {
    document.getElementById("packageName").value = name;

    document.getElementById("selectedPackage").value = price;
    document.getElementById("totalCost").textContent =
        "Estimated Total: ₹" + price.toLocaleString("en-IN");

    document.getElementById("booking").scrollIntoView({
        behavior: "smooth"
    });
}


// Booking enquiry form

document.getElementById("bookingForm").addEventListener("submit", function(event) {

    event.preventDefault();

    const name = document.getElementById("customerName").value.trim();
    const phone = document.getElementById("customerPhone").value.trim();
    const packageName = document.getElementById("packageName").value;

    if (!/^[0-9]{10}$/.test(phone)) {
        alert("Please enter a valid 10-digit phone number.");
        return;
    }

    if (!packageName) {
        alert("Please select a package first.");
        return;
    }

    document.getElementById("bookingMessage").textContent =
        "Thank you, " + name +
        "! Your " + packageName +
        " enquiry has been validated.";

    this.reset();
});
