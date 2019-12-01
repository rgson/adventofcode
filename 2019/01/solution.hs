#!/usr/bin/runghc

main :: IO ()
main = do
    input <- readFile "input.txt"
    putStrLn $ task1 input
    putStrLn $ task2 input

task1 :: String -> String
task1 input =
    show $ sum $ map fuel $ masses input

task2 :: String -> String
task2 input =
    show $ sum $ map fuel_recursive $ masses input

masses :: String -> [Int]
masses input = map read $ lines input

fuel :: Int -> Int
fuel mass = mass `div` 3 - 2

fuel_recursive :: Int -> Int
fuel_recursive mass =
    let f = fuel(mass)
    in if f > 0 then f + fuel_recursive(f) else 0
