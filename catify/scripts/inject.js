chrome.storage.local.get(["image"], async function (result) {
    if (result.image) {
        document.body.style.backgroundImage = `url(${result.image})`;
        document.body.style.backgroundSize = '200px'; // '200px' 대신에 '200px 200px'와 같이 너비와 높이를 설정해야 합니다.
        document.body.style.backgroundRepeat = 'repeat'; // 'repeat' 대신에 'repeat-x' 또는 'repeat-y'와 같이 반복 방향을 설정해야 합니다.
        console.log("image", result.image);
    }
    else {
        console.log("No image found in storage");
    }
    
});

