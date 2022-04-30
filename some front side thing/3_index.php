<?php

//set default values to be used when page first loads
$scores = array();
$scores[0] = 70;
$scores[1] = 80;
$scores[2] = 90;
        
$scores_string = '';
$score_total = 0;
$score_average = 0;
$max_rolls = 0;
$average_rolls = 0;

//take action based on variable in POST array
$action = filter_input(INPUT_POST, 'action');
switch ($action) {
    case 'process_scores':
        break;
    case 'process_rolls':
        $number_to_roll = filter_input(INPUT_POST, 'number_to_roll', 
                FILTER_VALIDATE_INT);
        $total = 0;
        $count = 0;
        $max_rolls = -INF;

        // TODO: convert this while loop to a for loop
        for($count=0;$count < 10000;$count++) {
            $rolls = 1;
            while (mt_rand(1, 6) != 6) {
                $rolls++;
            }
            $total += $rolls;
            $count++;
            $max_rolls = max($rolls, $max_rolls);
        }
        $average_rolls = $total / $count;

        break;
}
include 'loop_tester.php';
?>