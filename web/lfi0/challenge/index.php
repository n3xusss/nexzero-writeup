<?php

if (isset($_GET['page'])){
	include('/var/www/html/'.$_GET['page']);
}
else{

echo "<p>welcome to my secure website</p>";
echo "<p>choose a page : </p>";
echo "<ul>
	<li>
		<a href='/?page=home.php'>Home</a>
	</li>
	<li>
		<a href='/?page=about.php'>about</a>
	</li>
      </ul>";
}
?>
