<?php
/***
 * EXERCISE
 * Create a function that detects a cycle in a graph.
 */

class CycleDetector
{
    // Using constants for the three states node traveral instead of mere integers
    // makes our code more human-readable.
    private const STATE_UNVISITED = 0;
    private const STATE_VISITING = 1;
    private const STATE_VISITED = 2;

    // Storage for the state flag for each node.
    private static $states = [];

    /**
     * Helper function to preform a depth-first search for each node.
     * @param int $node The node number in the graph.
     * @param array $graph The full graph, which we pass to every call of this function.
     * @return bool
     */
    private static function dfs(int $node, array $graph): bool
    {
        // Change the node flag to indicate that we have started to process it.
        self::$states[$node] = self::STATE_VISITING;

        // Search all of the nodes neighbors.
        foreach ($graph[$node] as $neighbor) {
            // Get the state of the neighboring node.
            $neighborState = self::$states[$neighbor] ?? self::STATE_UNVISITED;
            // If we've run into a node that we are already processing, we've found a cycle.
            if ($neighborState == self::STATE_VISITING) { 
                return true;
            // If the neighbor is unvisited, start searching it in the same manner.
            } else if ($neighborState == self::STATE_UNVISITED) { 
                if (self::dfs($neighbor, $graph)) {
                    return true;
                }
            }
         }

         // Mark the node as fully processed.
         self::$states[$node] = self::STATE_VISITED;
         // If we've reached this point, we didn't find a cycle from this section.
         return false;
    }

    /**
     * Detect if the graph contains a cycle.
     * @param array $graph
     * @return bool
     */
    public static function hasCycle(array $graph): bool
    {
        // Initialize all nodes as unvisited.
        foreach(array_keys($graph) as $node) {
            self::$states[$node] = self::STATE_UNVISITED;
        }

        // Apply our dfs function to every node.
        foreach(array_keys($graph) as $node) {
            // We only need to check if we haven't already. This is just in case
            // the graph is disjointed.
            if (self::$states[$node] == self::STATE_UNVISITED) {
                if (self::dfs($node, $graph)) {
                    return true;
                }
            }
        }

        return false;
    }
}

// Example usage
if (get_included_files()[0] == __FILE__) {
    $myGraph = [
        0 => [1, 2],
        1 => [2],
        2 => [3],
        3 => [5, 6],
        4 => [6],
        5 => [],
        6 => [7, 8],
        7 => [],
        8 => [],
        9 => [10, 11],
        10 => [11],
        11 => [9],
    ];

    if (CycleDetector::hasCycle($myGraph)) {
        echo "Cycle detected.\n";
    } else {
        echo "No cycle found.\n";
    }
}