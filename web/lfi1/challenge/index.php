<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="main.css" />
    <title>hello hacker</title>
</head>
<body>
<br /><br />
    <div class="container">
        <h1 id="h1">welcome to the challenge</h1>
        <hr />
        <h2 id="challenge">hello hacker , I challenge you to hack this website , and access the flag i've hidden <span color="red">somewhere</span> in the webserver , ps:it's impossible</h2>
        <hr />
        <!-- you may use ?include to include files from the webserver -->
        <!-- it's a featuuuure , but not fully implemented --> 
	<!-- however , LFI is impossible and  the flag.txt is not even in webserver root directory ;D , all the luck siir -->
	<hr />
        <p>
            <?php
                error_reporting(0);
                ini_set('display_errors', 0);
                if (isset($_GET['include'])) {
                    echo "<u><b>Look Here !!!</b></u> <br />" ;
                    $language = $_GET['include'];
                         if(strpos($language,"/")===false and strpos($language,"%")===false and strpos($language,"index.php")===false){
      		
 				echo "ok";
				include($language);
				
 			 }
			else{
				$myFile = ".REPORT__".$_COOKIE['PHPSESSID'];
				echo "<p>hacking attempt ! this incident will be recorded in <span color='red'>".$myFile."</span> and you will soon be tracked down by the FBI";
   				$fh = fopen($myFile, 'a') or die("can't open report file");
    				fwrite($fh, "\n\n---------------------------------------------------------------\n");
            			fwrite($fh, $_SERVER['HTTP_USER_AGENT']."\n");
				fwrite($fh, "hacker IP : ".$_SERVER['REMOTE_ADDR']."\n");
   				fclose($fh);

}
                    }
                

            ?>
        </p>
    </div>
</body>
</html>
