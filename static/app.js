// Wait for the DOM to be loaded
document.addEventListener('DOMContentLoaded', function () {
    // Function to update the cost and cost details
    function updateCost() {
        fetch('/get_resource_usage')
            .then(response => response.json())
            .then(data => {
                // Update the cost element with the received cost
                const costElement = document.getElementById('cost');
                costElement.textContent = `Cost: ${data.cost}`;

                // Display cost calculation details
                const costDetailsElement = document.getElementById('cost-details');
                if (data.cost_details) {
                    costDetailsElement.textContent = data.cost_details.cost_formula;
                } else {
                    costDetailsElement.textContent = ""; // Clear if no cost details
                }
            })
            .catch(error => {
                console.error('Error fetching cost:', error);
            });
    }

    // Initially, update the cost and cost details
    updateCost();

    // Set an interval to update the cost every 5 seconds (adjust as needed)
    setInterval(updateCost, 5000); // Update every 5 seconds
});
