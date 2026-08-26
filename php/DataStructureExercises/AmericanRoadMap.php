<?php
/***
 * EXERCISE
 * Create a class that loads a road map of distances between cities, and create a 
 * method that finds the shortest path between two cities.
 */

namespace Aksman\Exercises\php\DataStructureExercises;

class AmericanRoadMap
{
    /**
     * Summary of map
     * @var array An associative 2D array with distances between cities.
     */
    private array $map = [];

    /**
     * Load the "map" from a file.
     * @param string $filename
     * @return AmericanRoadMap Returns itself to enable chaining.
     */
    public function load(string $filename): AmericanRoadMap
    {
        // Load the entire contents of the file as a string.
        $fileContents = file_get_contents($filename);

        // Convert the JSON string into an associative array. Note that the second argument
        // is set to true, making the output an associative array. By default, json_decode() 
        // converts a JSON string into an object.
        $this->map = json_decode($fileContents, true);

        // This is to enable chaining.
        return $this;
    }

    /**
     * Class constructor
     * @param string $filename Optional road map file to load on initialization.
     */
    public function __construct(string $filename='')
    {
        if ($filename) {
            $this->load($filename);
        }
    }

    /**
     * An implementation of Dijkstra's shortest path algorithm
     * @param string $city1 The starting city
     * @param string $city2 The destination city
     * @return array        The first element is the distance of the shortest path, and the second element 
     *                      is a sequential array showing the city-by-city path.
     */
    public function shortestPath(string $city1, string $city2): array 
    {
        // $visited: whether we have "visited" the city in our path traversal.
        // $prev: the city we come from in the shortest known path from the starting city.
        // $distance: the shortest known distance from the starting city.
        $visited = [];
        $prev = [];
        $distance = [];

        foreach(array_keys($this->map) as $city) {
            $visited[$city] = false;            
            $prev[$city] = NULL;
            if ($city == $city1) {
                $prev[$city] = $city;
                $distance[$city] = 0;
            } else {
                $prev[$city] = NULL;
                $distance[$city] = INF; // Initialize all other distances to infinity
            }
        }

       do {          
            // Filter out all the cities we've visited, and select the city with the shortest known 
            // distance to the starting city.
            $unvisited = array_filter($distance, fn($city) => !$visited[$city], ARRAY_FILTER_USE_KEY);           
            $currentCity = array_search(min($unvisited), $unvisited);

            // Loop through all the nodes of the current city.
            foreach($this->map[$currentCity] as $nextCity => $mileage) {
                // If the total distance is less than the distance we have recorded, set the distance 
                // to reflect the new shorter path, and set our traceback path ($prev) to the current city.
                if ($distance[$currentCity] + $mileage < $distance[$nextCity]) {
                    $distance[$nextCity] = $distance[$currentCity] + $mileage;
                    $prev[$nextCity] = $currentCity;
                }
            }
            // Now that we've processed the nodes in this city, mark it as visited.
            $visited[$currentCity] = true;

        // If we've reached our destination, we don't need to go any farther.
        } while ($currentCity != $city2);

        // Use the traceback ($prev) to find the path from the starting city to the destination.
        $path = [];
        $currentCity = $city2;
        while ($currentCity != $city1) {
            array_unshift($path, $currentCity);
            $currentCity = $prev[$currentCity];
        } 
        array_unshift($path, $currentCity);

        // Return the distance as an integer and the path as a sequential array.
        return [$distance[$city2], $path];
    }
}

// Example usage
// This block only runs if the script is run directly, i.e. not included.
if (get_included_files()[0] == __FILE__) {
    $city1 = $argv[1] ?? 'Cleveland, OH';
    $city2 = $argv[2] ?? 'Atlanta, GA';
    $filename = $argv[3] ?? 'USInterstateDistances.json';
    $map = new AmericanRoadMap($filename);
    [$distance, $path] = $map->shortestPath($city1, $city2);
    echo "Distance: {$distance} miles\n";
    echo 'Path: ' . implode(' -> ', $path);

}