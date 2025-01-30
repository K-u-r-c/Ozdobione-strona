function previewImage(input) {
  const file = input.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const img = document.createElement("img");
      img.src = e.target.result;
      img.style.maxWidth = "500px";
      img.style.maxHeight = "500px";
      const previewContainer = document.getElementById("image-preview");
      if (previewContainer) {
        previewContainer.innerHTML = "";
        previewContainer.appendChild(img);
      } else {
        const newPreviewContainer = document.createElement("div");
        newPreviewContainer.id = "image-preview";
        newPreviewContainer.appendChild(img);
        input.parentNode.appendChild(newPreviewContainer);
      }
    };
    reader.readAsDataURL(file);
  }
}
