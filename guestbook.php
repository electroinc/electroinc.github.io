<!DOCTYPE html>

<html>
<head>
<title>Guestbook</title>
<link rel="stylesheet" href="electroinc.css">
<link href="http://fonts.cdnfonts.com/css/negative-tuning" rel="stylesheet">
</head>

<body>

<iframe src="zapsound.mp3" type="audio/mp3" allow="autoplay" id="audio" style="display:none"></iframe>
<audio autoplay>
    <source src="zapsound.mp3" type="audio/mp3">
</audio>

	<div class="header">
	<div class="card">
		<image class="titleimage1" src="electricity.gif" title="ELECTRICITY" />
		<image src="title.png" />
		<image class="titleimage2" src="electricity.gif" title="MORE ELECTRICITY" />
	</div>
	</div>

	<div class="row">
	<div class="cardslim">
	<image src="homegif.gif" title="HOME"> <!-- cooltext.com laserian aab size 70 colour #6FFF00 flame angle 0 -->
	</div>
	</div>
	
	<div class="row">
		<div class="column left">
		<div class="card">


			<ul>
			<li><a href="homepage.html">Home</a></li>
			<li><a href="projects.html">Projects</a></li>
			<li><a href="tutorials.html">Tutorials</a></li>
			<li><a href="other.html">Other</a></li>
			<li><a href="updates.html">Updates</a></li>
			<li><a href="links.html">Links</a></li>
			</ul>
		</div>
		</div>

		<div class="column right">
		<div class="card">
			<p>Guestbook here.</p>
			<div>Test</div>
			<?php
				//connect to the database
				mysql_connect("localhost:3306", "ElecUsertroinc", "opampamplifier");
				mysql_select_db("elecefsv_guestbook");
				
				//Forms
				
				
				
				//Display
				$query = mysql_query("SELECT * FROM guestbook ORDER BY id DESC");
				$numrows = mysql_num_rows($query);
				if($numrows > 0){
					while($row = mysql_fetch_assoc($query)){
						$id = $row['id'];
						$name = $row['name'];
						$email = $row['email'];
						$message = $row['message'];
						$time = $row['time'];
						$date = $row['date'];
						$ip = $row['ip'];
						
						echo "<div><font color: white>
							$name - at $time on $date </ hr>
							$message </font>
						</div>";
						
					}
				}
				else {
					echo "No posts were found. ;-;";
				}
				
				mysql_close();
			?>
		</div>
	</div>
	
	<div class="footer">
	<p>You can use the information on this website at your own risk. I take <span style="color: red"> no responsibility </span> for damage/harm that results from copying info 
	from this websites. Companies/organisations are not allowed to use anything from this website to make money/clicks/increase profile,etc.</p>
	</div>

</body>
</html>

