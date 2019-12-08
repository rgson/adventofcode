#!/usr/bin/runghc

import Data.Char
import Data.List
import Data.Ord

main :: IO ()
main = do
    input <- readFile "input.txt"
    putStrLn $ task1 input
    putStrLn $ task2 input

task1 :: String -> String
task1 input =
    let
        (width, height) = (25, 6)
        layers = chunks (width * height) $ rstrip input
        layer = minimumBy (comparing $ countElem '0') $ layers
    in
        show $ (countElem '1' layer) * (countElem '2' layer)

task2 :: String -> String
task2 input =
    let (width, height) = (25, 6)
    in drawImage width $ decodeImage (width, height) $ rstrip input

rstrip :: String -> String
rstrip =
    reverse . dropWhile isSpace . reverse

countElem :: Eq a => a -> [a] -> Int
countElem x xs =
    length $ elemIndices x xs

chunks :: Int -> [a] -> [[a]]
chunks _ [] = []
chunks n xs =
    let (chunk, rest) = splitAt n xs
    in chunk : chunks n rest

decodeImage :: (Int, Int) -> String -> String
decodeImage (width, height) encodedImg =
    let
        layers = chunks (width * height) encodedImg
        pixel_layers = transpose layers
    in
        map (head . dropWhile (== '2')) pixel_layers

drawImage :: Int -> String -> String
drawImage width img =
    intercalate "\n" $ chunks width $ map color img

color :: Char -> Char
color '0' = 'X'
color '1' = '_'
color '2' = ' '
