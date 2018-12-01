[![Build Status](https://travis-ci.com/Vladius25/Haffman.svg?branch=master)](https://travis-ci.com/Vladius25/Haffman)
[![Лицензия на исходный код](https://img.shields.io/badge/license-GNU_GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.ru.html)

# Haffman
In computer science and information theory, a Huffman code is a particular type of optimal prefix code that is commonly used for lossless data compression. The process of finding and/or using such a code proceeds by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".

The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source symbol (such as a character in a file). The algorithm derives this table from the estimated probability or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy encoding methods, more common symbols are generally represented using fewer bits than less common symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number of input weights if these weights are sorted. However, although optimal among methods encoding symbols separately, Huffman coding is not always optimal among all compression methods.

[More](https://en.wikipedia.org/wiki/Huffman_coding)
