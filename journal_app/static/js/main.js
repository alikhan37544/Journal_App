document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const title = form.elements['title'].value.trim();
        const content = form.elements['content'].value.trim();

        if (title === '' || content === '') {
            event.preventDefault();
            alert('Please fill in all fields.');
        }
    });
});
