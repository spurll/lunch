<!doctype html>
<html>
	<head>
		<meta charset="utf-8"/>

		<?php
//			$games = array( "Diablo III", "Cargo Noir", "Shadows Over Camelot", "Red Dragon Inn", "Cosmic Encounter", "Power Grid", "Endeavor", "Puzzle Strike", "Last Night on Earth", "Magic: the Gathering", "Mansions of Madness", "Dominant Species", "Small World", "Pandemic", "Dominion", "Ascension", "Race for the Galaxy" );
			$games = array( "Diablo III", "Cosmic Encounter", "Power Grid", "Endeavor", "Puzzle Strike", "Magic: the Gathering", "Magic (EDH/Commander)", "Magic (Draft/Sealed)", "Dominant Species", "Pandemic", "Dominion", "Ascension", "Midgard", "Race for the Galaxy", "Tetrinet" );
			$winners = 3;

			function best( $input )
			{
				$counted = array_count_values( $input );
				arsort( $counted );
				return( key( $counted ) );
			}

			function worst( $input )
			{
				$counted = array_count_values( $input );
				asort( $counted );
				return( key( $counted ) );
			}

			function share( $array, $value )
			{
				$counted = array_count_values( $array );
				return( $counted[$value] / count( $array ) );
			}

			function remove( $array, $value )
			{
				if( ( $index = array_search( $value, $array ) ) !== false )
				{
					array_splice( $array, $index, 1 );
				}
				return( $array );
			}

			$selected = $_GET['selected'];
			if( $selected == '' ) { $selected = array(); }
			else { $selected = explode( ",", $selected ); }

			$available = array();
			for( $i = 0; $i < count( $games ); $i++ )
			{
				if( !in_array( $i, $selected ) ){ array_push( $available, $i ); }
			}

			$ballot = $_GET['submit'];
			$burn = ( $_GET['burn'] == 'true' ) || ( $_GET['burn'] == '1' );
			$debug = ( $_GET['debug'] == 'true' ) || ( $_GET['debug'] == '1' );
		?>

		<title>Games Day Voter!</title>
		<link rel="shortcut icon" href="GD.png"/>
		<style type="text/css">
			@font-face { font-family: CarbonType; src: url( 'Carbon.ttf' ); }
			@font-face { font-family: Bleeding Cowboys; src: url( 'BleedingCowboys.ttf' ); }

			.title { font-family: Bleeding Cowboys; font-size: 250%; color: #770000; }
			.header { font-family: Bleeding Cowboys; }
			.highlight { color: #aa0000 !important; }

			.login { height: 100px; color: #ffffff; }
			.window { width: 640px; margin: auto; }
			.footer { padding-top: 80px; color: #ffffff; width: 100%; }
			<?php echo '.games { text-align: left; vertical-align: top; font-size: '.( 14 / count( $games ) * 100 ).'%; }' ?>

			a:link { text-decoration: none; color: #000000; }
			a:visited { text-decoration: none; color: #000000; }
			a:hover { text-decoration: none; color: #770000; }
			a:active { text-decoration: none; color: #000000; }

			body { background: #330000 url('ParchmentSmall.png') no-repeat center top; color: #000000; overflow-y:auto; text-align: center; font-family: CarbonType, Courier New; }
		</style>
	</head>
	<body>
		<div class="window">
			<div class="login">
				<?php
					include("Login.php");

					$file = $data['username'].".vogt";

					/* Submit ballot. */
					if( $ballot != '' )
					{
						$handle = fopen( $file, 'w' ) or die( "Unable to open $file for writing." );
						fwrite( $handle, $ballot );
						fclose( $handle );
					}

					/* Burn ballot. */
					if( $burn )
					{
						unlink( $file );
					}
				?>
			</div>

			<div class="title">Games Day Voter</div>

			<div style="height: 410px">
				<div style="width: 50%; float: left;">
					<div class="header">
						Available Games
					</div>
					<div class="games" style="height: 260px;">
						<?php
							for( $i = 0; $i < count( $available ); $i++ )
							{
								if( count( $selected ) == 0 )
								{
									echo '<div><a href="index.php?selected='.$available[$i].'">'.$games[$available[$i]].'</a></div>';
								}
								else
								{
									echo '<div><a href="index.php?selected='.implode( ',', $selected ).','.$available[$i].'">'.$games[$available[$i]].'</a></div>';
								}
							}
						?>
					</div>
					<div class="header">
						<a href="index.php?burn=true"><img src="BurnBallotColourOutline.png" height="145"/></a>
					</div>
				</div>
				<div style="width: 50%; float: right;">
					<div class="header">
						Ballot
					</div>
					<div class="games" style="height: 260px;">
						<?php
							for( $i = 0; $i < count( $selected ); $i++ )
							{
								echo '<div><a href="index.php?selected='.implode( ',', remove( $selected, $selected[$i] ) ).'">'.($i+1).'. '.$games[$selected[$i]]."</a></div>";
							}
						?>
					</div>
					<div class="header">
						<?php
							echo '<a href="index.php?submit='.implode( ',', $selected ).'"><img src="VoteSeal.png" width="132" height="119"/></a>';
						?>
					</div>
				</div>
			</div>
			<div class="footer">
				<?php
					$allBallots = array();
					foreach( glob( '*.vogt' ) as $file )
					{
						$handle = fopen( $file, 'r' ) or die( "Unable to open $file for reading." );
						array_push( $allBallots, fread( $handle, filesize( $file ) ) );
						fclose( $handle );
					}
					$uniqueGames = count( array_unique( explode( ',', implode( ',', $allBallots) ) ) );
					$winners = min( $winners, $uniqueGames );

					if( count( $allBallots ) > 0 )
					{
						echo '<div>Winning Game:</div>';
						echo '<div class="highlight">';
						for( $w = 0; $w < $winners; $w++ )
						{
							$ballots = $allBallots;

							$share = 0;
							$loser = -1;
							$winner = -1;
							while( ( $share <= 0.5 ) && ( count( $ballots ) > 0 ) )
							{
								if( ( $debug ) && ( $loser >= 0 ) ){ echo '<div>Eliminating <span style="color: #ffffff;">'.$games[$loser].'</span> ('.$loser.').</div>'; }
								$vogts = array();
								for( $i = 0; $i < count( $ballots ); $i++ )
								{
									$ballots[$i] = preg_replace( "/(^$loser$)|(^$loser,)|(,$loser$)/", "", $ballots[$i] );
									$ballots[$i] = preg_replace( "/,$loser,/", ",", $ballots[$i] );
									$ballot = explode( ',', $ballots[$i] );
									if( $ballot[0] !== '' ){ array_push( $vogts, $ballot[0] ); }
								}
								if( $debug ){ echo '<div>Votes: '.implode( ', ', $vogts ).'</div>'; }

								$winner = best( $vogts );
								$share = share( $vogts, $winner );
								$loser = worst( $vogts );
							}

							if( $w == 1 ){ echo '<div style="color: #ffffff;"><br/>Runners Up:</div>'; }
							echo $games[$winner];
							if( $debug ){ echo sprintf( " (%.0f)", $share * 100 ); }
							echo '<br/>';

							for( $i = 0; $i < count( $allBallots ); $i++ )
							{
								$allBallots[$i] = preg_replace( "/(^$winner$)|(^$winner,)|(,$winner$)/", "", $allBallots[$i] );
								$allBallots[$i] = preg_replace( "/,$winner,/", ",", $allBallots[$i] );
							}
						}
						echo '</div>';
					}
				?>
			</div>
		</div>
	</body>
</html>