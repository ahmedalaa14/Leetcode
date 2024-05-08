func guessNumber(n int) int {
\treturn binarySearch(0, n)
}

func binarySearch(start, finish int) int {
\tif start > finish {
\t\treturn -1
\t}
\tdot := (finish-start)/2 + start

\tswitch guess(dot) {
\tcase -1:
\t\treturn binarySearch(start, dot-1)
\tcase 1:
\t\treturn binarySearch(dot+1, finish)
\tdefault:
\t\treturn dot
\t}
}