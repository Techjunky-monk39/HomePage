document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            document.querySelector(targetId).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Handle contact form submission using EmailJS
    document.getElementById('contactForm').addEventListener('submit', async (event) => {
        event.preventDefault();
        const messageDisplay = document.getElementById('message-display');
        messageDisplay.className = '';
        messageDisplay.textContent = 'Sending...';

        const name = document.querySelector('#name').value.trim();
        const email = document.querySelector('#email').value.trim();
        const message = document.querySelector('#message').value.trim();

        if (!name || !email || !message) {
            messageDisplay.textContent = 'Please fill in all fields.';
            messageDisplay.classList.add('error');
            return;
        }
        
        const emailMessage = {
            from_name: name,
            from_email: email,
            message: message
        };

        try {
            await emailjs.send('default_service', 'template_contact1', emailMessage);
            messageDisplay.textContent = 'Your message has been sent successfully!';
            messageDisplay.classList.add('success');
            document.getElementById('contactForm').reset();
        } catch (error) {
            console.error('Error:', error);
            messageDisplay.textContent = 'Failed to send your message. Please try again later.';
            messageDisplay.classList.add('error');
        }
    });
});