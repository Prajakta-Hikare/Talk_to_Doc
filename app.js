const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


document.addEventListener("DOMContentLoaded", function() {
  // Select the login form
  const loginForm = document.querySelector(".sign-in-form");

  // Add event listener for form submission
  loginForm.addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Perform your authentication logic here
    // For demonstration purposes, let's assume the user is authenticated successfully

    // Redirect the user to a new page
    window.location.href = "chat.html"; // Replace "welcome.html" with the URL of your welcome page
  });
});