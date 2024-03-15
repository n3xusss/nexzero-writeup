<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome to the Dark Web</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      background: url('darkweb.png') center/cover no-repeat fixed;
      color: #fff;
      font-family: 'Arial', sans-serif;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    h1 {
      font-size: 3em;
      margin-bottom: 20px;
      text-shadow: 2px 2px 4px #000;
    }

    p {
      font-size: 1.5em;
      text-shadow: 1px 1px 2px #000;
    }
  </style>
</head>
<body>
  <div id="delayedParagraph" style="display: none;">
  <h1>Welcome to the Dark Web</h1>
  <p>nexus{d4rk_WeB_Do3snt_Us3_dNS_r1GHt?}</p>
  </div>
  <script>
    function showParagraphAfterImageLoad() {
      // Create a new Image object
      var backgroundImage = new Image();

      // Set the source of the background image
      backgroundImage.src = 'darkweb.png';

      // Use the onload event to wait for the image to be loaded
      backgroundImage.onload = function() {
        // Get the paragraph element by its id
        var paragraph = document.getElementById('delayedParagraph');

        // Show the paragraph by changing its style display property
        paragraph.style.display = 'block';
      };
    }

    // Call the function to start the process
    showParagraphAfterImageLoad();
  </script>

</body>
</html>