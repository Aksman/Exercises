<?php
/***
 * EXERCISE
 * Create a class that documents security vulnerabilities in code, prioritizing by severity.
 */

namespace Aksman\Exercises\php\DataStructureExercises;

use SplPriorityQueue;

/**
 * This is accomplished very easily by extending PHP's own built-in SplPriorityQueue class.
 */
class SecurityVulnerabilityLogger extends SplPriorityQueue
{
    // All we add is a set of class constants representing the log levels.
    const INFO = 0;
    const LOW = 1;
    const MODERATE = 2;
    const HIGH = 3;
    const CRITICAL = 4;

}

if (get_included_files()[0] == __FILE__) {
    $logger = new SecurityVulnerabilityLogger();

    // The insert() method is inherited from the SplPriorityQueue class. It accepts a value 
    // (in this case a string description of the issue) and a priority.
    $logger->insert('XSS vulnerability', SecurityVulnerabilityLogger::MODERATE);
    $logger->insert('Unnecessarily verbose error message', SecurityVulnerabilityLogger::LOW);
    $logger->insert('Remote code execution vulnerability', SecurityVulnerabilityLogger::CRITICAL);
    $logger->insert('Sensitive data exposure', SecurityVulnerabilityLogger::MODERATE);
    $logger->insert('SQL injection vulnerability', SecurityVulnerabilityLogger::HIGH);
    $logger->insert('Style guide deviation', SecurityVulnerabilityLogger::INFO);
    $logger->insert('Denial of Service exploit', SecurityVulnerabilityLogger::MODERATE);
    $logger->insert('Privilege escalation vulnerability', SecurityVulnerabilityLogger::CRITICAL);

    // The SplPriorityQueue is countable.
    echo "Number of issues found: " . count($logger) . "\n";
    
    // The SplPriorityQueue is also iterable. Note that the critical issues are output first, then
    // in descending order of priority.
    foreach($logger as $entry) {
        echo $entry . "\n";
    }
}