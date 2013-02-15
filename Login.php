<?php
	$realm = 'Games Day Voter';

	// User => Password
//	$users = array( 'gem' => 'strike', 'brendan' => '7Fwy75Mt', 'mike' => '?DAjVPE3', 'eric' => 'rL9BRwPm', 'bhavek' => '6a2VeHmK', 'curt' => 'Jrmp0kbw', 'aron' => 'g0ghLcng', 'ali' => 'EVrbSm9q', 'matt' => '7lPoL0yQ', 'nick' => '7lPooooQ' );
	$users = array( 'gem' => 'strike', 'brendan' => '', 'mike' => '', 'eric' => '', 'bhavek' => '', 'curt' => '', 'aron' => '', 'ali' => '', 'matt' => '', 'nick' => '', 'dale' => '', 'dustin' => '', 'cozmin' => '' );

	if ( empty( $_SERVER['PHP_AUTH_DIGEST'] ) )
	{
		header( 'HTTP/1.1 401 Unauthorized' );
		header( 'WWW-Authenticate: Digest realm="'.$realm.'",qop="auth",nonce="'.uniqid().'",opaque="'.md5($realm).'"' );
		die( 'You are not authorised to view this page.' );
	}

	// Analyze the PHP_AUTH_DIGEST variable.
	if ( !( $data = http_digest_parse( $_SERVER['PHP_AUTH_DIGEST'] ) ) || !isset( $users[$data['username']] ) )
	{
		header( 'HTTP/1.1 401 Unauthorized' );
		header( 'WWW-Authenticate: Digest realm="'.$realm.'",qop="auth",nonce="'.uniqid().'",opaque="'.md5($realm).'"' );
		die( 'Invalid credentials or no user name supplied!' );
	}

	// Generate the valid response.
	$A1 = md5( $data['username'].':'.$realm.':'.$users[$data['username']] );
	$A2 = md5( $_SERVER['REQUEST_METHOD'].':'.$data['uri'] );
	$valid_response = md5( $A1.':'.$data['nonce'].':'.$data['nc'].':'.$data['cnonce'].':'.$data['qop'].':'.$A2 );

	if ( $data['response'] != $valid_response )
	{
		header( 'HTTP/1.1 401 Unauthorized' );
		header( 'WWW-Authenticate: Digest realm="'.$realm.'",qop="auth",nonce="'.uniqid().'",opaque="'.md5($realm).'"' );
		die( $data['response'].'Invalid credentials!'.$valid_response );
	}

	// Valid username & password.
	echo 'You are logged in as <span class="highlight">'.$data['username'].'</span>.';

	// Function to parse the http auth header.
	function http_digest_parse( $txt )
	{
		// Protect against missing data.
		$needed_parts = array( 'nonce'=>1, 'nc'=>1, 'cnonce'=>1, 'qop'=>1, 'username'=>1, 'uri'=>1, 'response'=>1 );
		$data = array();
		$keys = implode( '|', array_keys( $needed_parts ) );

		preg_match_all( '@('.$keys.')=(?:([\'"])([^\2]+?)\2|([^\s,]+))@', $txt, $matches, PREG_SET_ORDER );

		foreach ( $matches as $m ){
			$data[$m[1]] = $m[3] ? $m[3] : $m[4];
			unset( $needed_parts[$m[1]] );
		}

		return $needed_parts ? false : $data;
	}
?>