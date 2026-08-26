<?php
/***
 * EXERCISE
 * Create a function that calculates the least common multiple of two integers.
 */

namespace Aksman\Exercises\php\MathExercises;

// Explicitly include the gcd function we've defined in another file.
require_once('gcd.php');

/**
 * Find the least common multiple. This takes advantage of the fact that for any two natural numbers,
 * their product will be equal to their greatest common divisor multiplied by their least common multiple.
 * @param int $a
 * @param int $b
 * @return int
 */
function lcm(int $a, int $b): int 
{
    // Check for zero, to avoid divide by zero error.
    if ($a == 0 || $b == 0) {
        return 0;
    }
    return abs($a * $b) / gcd($a, $b);
}

// Example usage
if (get_included_files()[0] == __FILE__) {
    $a = (int)($argv[1] ?? 18);
    $b = (int)($argv[2] ?? 30);

    $m = lcm($a, $b);
    echo "LCM({$a}, {$b}) = {$m}";
}