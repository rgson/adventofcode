#!/usr/bin/runghc

import Data.List

main :: IO ()
main = do
    input <- readFile "input.txt"
    putStrLn $ task1 input
    putStrLn $ task2 input

task1 :: String -> String
task1 =
    show
    . length
    . filter hasDoubles
    . filter isIncreasing
    . map digits
    . parseRange

task2 :: String -> String
task2 =
    show
    . length
    . filter (any (== 2))
    . map groupLengths
    . filter isIncreasing
    . map digits
    . parseRange

parseRange :: String -> [Int]
parseRange range =
    let [start, end] = map read $ splitOn '-' range
    in [start .. end]

splitOn :: Char -> String -> [String]
splitOn delim str =
    case str of
        "" -> []
        s' -> let (x, s'') = break (== delim) s'
              in x : splitOn delim (drop 1 s'')

digits :: Int -> [Int]
digits n
    | n < 10 = [n]
    | otherwise = digits (n `div` 10) ++ [n `mod` 10]

pairMap :: (a -> a -> b) -> [a] -> [b]
pairMap f xs =
    zipWith f xs $ tail xs

isIncreasing :: Ord a => [a] -> Bool
isIncreasing xs =
    all id $ pairMap (<=) xs

hasDoubles :: Eq a => [a] -> Bool
hasDoubles xs =
    any id $ pairMap (==) xs

groupLengths :: Eq a => [a] -> [Int]
groupLengths xs =
    map length $ group xs
