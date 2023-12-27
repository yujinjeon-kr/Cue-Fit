document.getElementById('dalle-form').addEventListener('submit', function(e) {
    e.preventDefault();
  
    const promptText = document.getElementById('prompt').value;
    const generatedImageDiv = document.getElementById('generated-image');
  
    // OpenAI API 엔드포인트
    const apiUrl = 'https://api.openai.com/v1/images/generations';
  
    // OpenAI API 키 설정 (클라이언트 측 코드에 포함하는 것은 권장되지 않음)
    const api_key = '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';
  
    fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${api_key}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt: promptText, "n": 1, "size": "1024x1024", "model": "dall-e-3" })
    })
    .then(response => response.json())
    .then(data => {
      const imageUrl = data.data[0].url; // 생성된 이미지의 URL
      generatedImageDiv.innerHTML = `<img src="${imageUrl}" class="img-fluid" alt="Generated Image"/>`;
      
      // 다운로드 링크 추가
      const downloadLink = document.createElement('a');
      downloadLink.href = imageUrl;
      downloadLink.download = "generated_image.png"; // 다운로드될 파일명
      downloadLink.innerText = "이미지 다운로드";
      generatedImageDiv.appendChild(downloadLink);
    })
    .catch(error => console.error('Error:', error));
  });
  
  
  document.getElementById('image-upload').addEventListener('change', function(e) {
    if (e.target.files && e.target.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            document.getElementById('uploaded-image').innerHTML = 
                `<img src="${e.target.result}" class="img-fluid" alt="Uploaded Image"/>`;
        };
        reader.readAsDataURL(e.target.files[0]);
    }
  });
  