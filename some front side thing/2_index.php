<?php

//set default values to be used when page first loads
$scores = array();
$scores[0] = 70;
$scores[1] = 80;
$scores[2] = 90;
        
$scores_string = '';
$score_total = 0;
$score_average = 0;
$score_total_f=0;        // the formated total variable
$score_average_f=0;      // the formated average variable


//take action based on variable in POST array
$action = filter_input(INPUT_POST, 'action');
if($action=='process_scores')
{        $is_valid = true;
        $scores = $_POST['scores'];

        //add code that validate the scores,make sure enter three valid numbers for scores                
        /*if one of three scores is not valid, you can assign the variables: 
		$scores_string = 'You must enter three valid numbers for scores.';
		$is_valid = false;*/
		foreach ($scores as $s) {
		if(!isset($s)){
			$scores_string = 'You must enter three valid numbers for scores.';
              $is_valid = false;}}
        // process the scores
        // TODO: Add code that calculates the score total
		if( $is_valid ){
        $scores_string = '';
        foreach ($scores as $s) {
            $scores_string .= $s . '|';
        }
		for ($i=0;$i<3;$i++){
			$score_total=$scores[$i]+$score_total;
		}
        $scores_string = substr($scores_string, 0, strlen($scores_string)-1);
		$score_total_f=sprintf("%.2f",$score_total);
        // calculate the average
        $score_average =round($score_total / count($scores),2);
        
        // add code to format the total and average, round the number to two decimal places.
        $score_average_f=sprintf("%.2f",$score_average);
}
}
include 'loop_tester.php';
?>