<?php
include 'flag.php';
Class  Rumbling
{   
    public $name;
    public $steps = -1;
    function __construct($name){
        $this->name=$name;
    }
    public function __sleep() {
        eval('$this->steps='.strval($this->steps).'+1;');
        return ['name','steps'];
    }
}

if(isset($_POST['name'])){
    $rumbling=new Rumbling($_POST['name']);
    setcookie("ID", bin2hex(serialize($rumbling)), time() + 3600);
}
elseif (isset($_COOKIE['ID'])){
    $rumbling = unserialize(hex2bin($_COOKIE['ID']));
    if ($rumbling==False){
        echo "<div class='vertical-center'>
        <p>you are trying to cheat...</p>
        <p>how can you call yourself a soldier ? </p>
        ";
        die();
    }
}
if (isset($_POST["step"])&& isset($rumbling)){
    setcookie("ID", bin2hex(serialize($rumbling)), time() + 3600);
}
?>
<!DOCTYPE html>
<html lang="en">
<style>
input[type=text]:focus {
  background-color: lightblue;
}
.vertical-center {
    text-align: center;

}
h1 { color: #ffffff; font-family: 'Lato', sans-serif; font-size: 54px; font-weight: 300; line-height: 58px; margin: 0 0 58px; }
p { color: #adb7bd; font-family: 'Lucida Sans', Arial, sans-serif; font-size: 16px; line-height: 26px; text-indent: 30px; margin: 0; }
/* tatakae !*/ 
.button-62 {
  background: linear-gradient(to bottom right, #8d0505, #250909);
  border: 0;
  border-radius: 12px;
  color: #FFFFFF;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size: 16px;
  font-weight: 500;
  line-height: 2.5;
  outline: transparent;
  padding: 0 1rem;
  text-align: center;
  text-decoration: none;
  transition: box-shadow .2s ease-in-out;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
}
</style>
<head>
    <title>Rumbling</title>
</head>
<body style="background-image: url('rumbling.png');background-size: cover; background-repeat: no-repeat;">
<?php
if (isset($rumbling)){
        ?>
    <div class="vertical-center">
    <?php
        if ($rumbling->steps>=10){?>
            <p>you have now reached freedom</p>
            <p>but not the flag...</p>
            
        <?php }
        else{?>
        <p>keep mooving forward ... until your enemies are all destroyed</p>
        <?php }?>
        <p>steps done : <?=$rumbling->steps?></p>

    <form action="index.php" method="post">
        <br/>
        
        <button class="button-62" type="submit" name='step'>step forward</button>
        <h1></h1>
    </form>
    <!--keep moving forward... and you'll eventually reach the flag and your freedom-->
</div>
 <?php 
 
    
}
else{?>
    <div class="vertical-center">
        <p>keep mooving forward ... until your enemies are all destroyed</p>
    <form action="index.php" method="post">
        <br/>
        <p>what is your name soldier ? </p>
        <input type="text" name='name'></input>
        <h1></h1>
    </form>
    <?php
}
?>
</body>
</html>