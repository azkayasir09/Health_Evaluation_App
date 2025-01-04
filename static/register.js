// Select elements
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirm_password');
const passwordError = document.getElementById('passwordError');
const passwordSuccess = document.getElementById('passwordSuccess');
const form = document.getElementById('registrationForm');



// Form submission validation
form.addEventListener('submit', (event) => {
    if (password.value !== confirmPassword.value) {
        event.preventDefault();
        passwordError.style.display = 'block';
        passwordSuccess.style.display = 'none';
        alert("Passwords do not match. Please try again.");
    }
    else {
        alert("Form submitted successfully!");
    }
});
form.getElementById('login').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Logged In successfully!');
});
