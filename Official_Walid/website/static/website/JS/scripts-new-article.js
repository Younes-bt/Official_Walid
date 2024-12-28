

document.addEventListener('DOMContentLoaded', function () {
    // Get the category field and pdfID element
    const categoryField = document.getElementById('article-cat');
    const pdfField = document.getElementById('article-id');
    const labelId = document.getElementById('label-id');

    if (categoryField && pdfField) {
        // Function to update the pdfID display based on category value
        const updatePdfFieldDisplay = () => {
            const selectedValue = categoryField.value;
            if (selectedValue === '2') {
                pdfField.classList.add('d-none'); // Hide element
                labelId.classList.add('d-none'); // Hide element
                pdfField.classList.remove('d-flex'); // Remove display:flex
                labelId.classList.remove('d-flex'); // Remove display:flex
            } else if (selectedValue === '1') {
                pdfField.classList.add('d-flex'); // Show element
                labelId.classList.add('d-flex'); // Show element
                pdfField.classList.remove('d-none'); // Remove display:none
                labelId.classList.remove('d-none'); // Remove display:none
            }
        };

        // Trigger update on page load (optional)
        updatePdfFieldDisplay();

        // Add event listener for changes in the category field
        categoryField.addEventListener('change', updatePdfFieldDisplay);
    }
});

