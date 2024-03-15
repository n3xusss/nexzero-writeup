<!DOCTYPE html>
<html>
<head>
    <title>images upload</title>
</head>
<body>
    <h2>images upload</h2>
    
    <?php
    $uploadOk = 0;

    if (!is_dir('uploads')) {
        mkdir('uploads');
        chmod('uploads', 0777);
    }

    if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_FILES['file'])) {
        $filename = basename($_FILES["file"]["name"]);
        $target_dir = "uploads/";
        $target_file = $target_dir . $filename;
        
        // Check if image file is a actual image or fake image 
        $check = getimagesize($_FILES["file"]["tmp_name"]);
        if ($check === false) {
            exit(sprintf("%s is not an image", $filename));
        }
        
        // Check file size
        if ($_FILES["file"]["size"] > 2000000) {
            exit(sprintf("%s is too large", $filename));
        }
        
        // Attempt to move the uploaded file to the target directory
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
            $uploadOk = 1;
            echo "file successfully uploaded, you can find it at : /" . $target_file;
        } else {
            exit("Sorry, there was an error uploading your file.");
        }
    }
    ?>
    
    <form action="" method="post" enctype="multipart/form-data">
        Select image to upload (max 2MB):
        <input type="file" name="file" id="fileToUpload">
        <input type="submit" value="Upload Image" name="submit">
    </form>
</body>
</html>
