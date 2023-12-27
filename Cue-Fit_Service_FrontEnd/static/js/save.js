document.getElementById('combine-images-button').addEventListener('click', function() {
    var userImageInput = document.getElementById('user-image');
    var dalleImageInput = document.getElementById('dalle-image');
  
    if (!userImageInput.files[0] || !dalleImageInput.files[0]) {
        console.error("Both images must be selected.");
        return;
    }
  
    var formData = new FormData();
    formData.append('user-image', userImageInput.files[0]);
    formData.append('dalle-image', dalleImageInput.files[0]);
  
    fetch('combine_images', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.image_url) {
            document.getElementById('combined-image').innerHTML = 
                `<img src="${data.image_url}" class="img-fluid" alt="Combined Image"/>`;
        } else {
            console.error('Error in image combination');
        }
    })
    .catch(error => console.error('Error:', error));
  });
  
  