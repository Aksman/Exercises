<?php
/***
 * EXERCISE
 * Create a function that finds the prime factorization of a number, including the number of 
 * times each factor can be divided by the number (i.e. the exponents).
 */

namespace Aksman\Exercises\php\MathExercises;

require_once('primes.php');

function primeFactorize(int $number): array 
{
    if ($number < 2) {
        throw new \InvalidArgumentException('The value must be at least two.');
    }
    $factors = [];
    $primes = primes($number);
    foreach($primes as $p) {
        if ($p > $number) break;
        while ($number % $p == 0) {
            $factors[$p] = ($factors[$p] ?? 0) + 1;
            $number /= $p;
        }
    }
    return $factors;
}

// Example usage
if (get_included_files()[0] == __FILE__) {
    $number = (int)($argv[1] ?? 6132);

    $factorization = primeFactorize($number);
    echo "Factorization: "; 
    echo var_export($factorization);
}