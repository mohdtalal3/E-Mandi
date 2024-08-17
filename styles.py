# styles.py

fruit_vegetable_box_style = """
<div class="fruit-vegetable-box {1}" onclick="handleClick('{0}')">
    <h2>{0}</h2>
</div>
<style>
    .fruit-vegetable-box {{
        background-color: #f0f0f0;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        cursor: pointer;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .fruit-vegetable-box:hover {{
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}
    .fruit {{
        background-color: #ffcccb;
    }}
    .vegetable {{
        background-color: #90ee90;
    }}
</style>
<script>
    function handleClick(type) {{
        // This function will be called when a box is clicked
        // You can add custom JavaScript here if needed
        console.log(type + " clicked");
    }}
</script>
"""

grocery_item_style = """
<style>
    .grocery-item {{
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        text-align: center;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        cursor: pointer;
    }}
    .grocery-item:hover {{
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}
    .grocery-item img {{
        width: 100%;
        max-width: 200px;
        height: auto;
        border-radius: 5px;
        margin-bottom: 10px;
    }}
    .grocery-item h3 {{
        margin: 5px 0;
        color: #333;
    }}
    .grocery-item p {{
        margin: 5px 0;
        color: #666;
    }}
</style>
"""

search_bar_style = """
<style>
    .stTextInput > div > div > input {
        font-size: 20px;
        padding: 10px 15px;
    }
    .stSelectbox > div > div > div {
        font-size: 18px;
        padding: 5px 10px;
    }
</style>
"""
# styles.py

grocery_item_style = """
<style>

.grocery-item {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        cursor: pointer;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 250px;
    }
    .grocery-item:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .grocery-item img {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 10px;
    }
    .grocery-item h3 {
        margin: 10px 0;
        font-size: 18px;
    }
    .grocery-item p {
        margin: 5px 0;
        font-size: 14px;
    }



    .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.4);
    }
    .modal-content {
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 80%;
        max-width: 500px;
        border-radius: 10px;
    }
    .close {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
    }
    .close:hover,
    .close:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
</style>

<script>
function openModal(id) {
    document.getElementById(id).style.display = "block";
}

function closeModal(id) {
    document.getElementById(id).style.display = "none";
}

// Close the modal if clicked outside of it
window.onclick = function(event) {
    if (event.target.className === "modal") {
        event.target.style.display = "none";
    }
}
</script>
"""

# styles.py

add_new_button_style = """
<style>
    /* Style for the Add New Grocery expander */
    .add-new-expander {
        background-color: #4CAF50 !important;
        border: none !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 10px 20px !important;
        text-align: center !important;
        text-decoration: none !important;
        font-size: 20px !important;
        margin: 10px 0 !important;
        cursor: pointer !important;
        transition: all 0.3s !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
    }

    .add-new-expander:hover {
        background-color: #45a049 !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3) !important;
    }

    /* Style for the expander content */
    .add-new-expander .streamlit-expanderContent {
        background-color: white !important;
        border: 1px solid #4CAF50 !important;
        border-top: none !important;
        border-radius: 0 0 12px 12px !important;
    }

    /* Style for the expander header */
    .add-new-expander .streamlit-expanderHeader {
        color: white !important;
        background-color: transparent !important;
        font-weight: bold !important;
    }

    /* Style for the expander icon */
    .add-new-expander .streamlit-expanderHeader svg {
        fill: white !important;
    }
</style>
"""