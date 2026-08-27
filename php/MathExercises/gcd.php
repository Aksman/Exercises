<?php
/***
 * EXERCISE
 * Create a function that finds the greatest common divisor of two integers.
 */

namespace Aksman\Exercises\php\MathExercises;

/**
 * This uses the Euclidean Algorithm to calculate the GCD.
 * @param int $a
 * @param int $b
 * @return int
 */
function gcd(int $a, int $b): int
{
    // If the numbers are in the wrong order, switch them.
    if (abs($a) < abs($b)) {
        [$a, $b] = [$b, $a];
    }
    // If the smaller number is 0, then the GCD is 0.
    if ($b == 0) {
        return 0;
    }
    // Divide the larger number by the smaller number. If they divide evenly, then the smaller number 
    // is GCD. If not, try again with the smaller number and the remainder. Repeat the process until you find
    // numbers that divide evenly, at which point the smaller number will be the GCD.
    $r = $a % $b; 
    return $r ? gcd($b, $r) : abs($b);
}

// Example usage.
// This block only runs if the script is run directly, i.e. not included.
if (get_included_files()[0] == __FILE__) {
    $a = (int)($argv[1] ?? 72);
    $b = (int)($argv[2] ?? 18);

    echo "A: {$a}\n";
    echo "B: {$b}\n";
    
    $d = gcd($a, $b);
    echo "GCD: {$d}";
}