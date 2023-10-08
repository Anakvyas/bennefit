document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('symptom-form');
    const result = document.getElementById('result');

    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const symptoms = Array.from(document.getElementsByName('symptoms'))
            .filter(input => input.checked)
            .map(input => input.value);

        if (symptoms.length === 0) {
            result.innerHTML = 'Please select at least one symptom.';
        } else if (symptoms.length <= 2) {
            result.innerHTML = 'You may have some diabetic symptoms. Please consult a doctor for a proper diagnosis.';
        } else {
            result.innerHTML = 'It is highly recommended that you consult a doctor as you may have significant diabetic symptoms.';
        }
    });
});
