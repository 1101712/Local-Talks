document.addEventListener("DOMContentLoaded", function() {
    const passwordInput = document.getElementById("id_password1");
    const confirmPasswordInput = document.getElementById("id_password2");
    const emailInput = document.querySelector("input[name='email']");

    const passwordHint = document.createElement("p");
    const emailHint = document.createElement("p");
    
    passwordHint.id = "passwordHint";
    emailHint.id = "emailHint";
    
    passwordHint.style.color = "#76161eda";
    emailHint.style.color = "#76161eda";

    const accountInfo = document.querySelector("h3");
    accountInfo.parentNode.insertBefore(passwordHint, accountInfo.nextSibling);
    accountInfo.parentNode.insertBefore(emailHint, accountInfo.nextSibling);

    let confirmPasswordTouched = false;

    function validateForm() {
        let passwordErrors = [];
        let emailErrors = [];

        // Password validation
        const password = passwordInput.value;
        if (password.length < 8) passwordErrors.push("Password should be at least 8 characters long.");
        if (!/[A-Z]/.test(password)) passwordErrors.push("Password should contain at least one uppercase letter.");
        if (!/[a-z]/.test(password)) passwordErrors.push("Password should contain at least one lowercase letter.");
        if (!/[0-9]/.test(password)) passwordErrors.push("Password should contain at least one number.");
        if (!/[@$!%*?&#]/.test(password)) passwordErrors.push("Password should contain at least one special character (@, $, !, %, *, ?, &, #).");
        if (confirmPasswordTouched && password !== confirmPasswordInput.value) passwordErrors.push("Passwords do not match.");
        
        passwordHint.textContent = passwordErrors.join(" ");

        // Email validation
        const email = emailInput.value;
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

        if (!email.includes('@')) emailErrors.push("Please include an '@' in the email address.");
        if (!email.includes('.')) emailErrors.push("Please include a '.' in the email address.");
        if (!emailRegex.test(email)) emailErrors.push("Please use a valid domain for email address.");

        emailHint.textContent = emailErrors.join(" ");
    }

    passwordInput.addEventListener("input", validateForm);
    confirmPasswordInput.addEventListener("input", function() {
        confirmPasswordTouched = true;
        validateForm();
    });
    emailInput.addEventListener("input", validateForm);
});
