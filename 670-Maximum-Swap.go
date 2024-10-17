func maximumSwap(num int) int {
\tbyteNum := []byte(strconv.Itoa(num))
\tvar pivot int
\tfor pivot = 0; pivot < len(byteNum)-1; pivot++ {
\t\tif byteNum[pivot] < byteNum[pivot+1] {
\t\t\tbreak
\t\t}
\t}
\tif pivot == len(byteNum)-1 {
\t\treturn num
\t}

\tto := pivot
\tfor i := pivot + 1; i < len(byteNum); i++ {
\t\tif byteNum[i] >= byteNum[to] {
\t\t\tto = i
\t\t}
\t}
\tfrom := pivot
\tfor i := pivot - 1; i >= 0; i-- {
\t\tif byteNum[i] < byteNum[to] {
\t\t\tfrom = i
\t\t}
\t}

\tbyteNum[from], byteNum[to] = byteNum[to], byteNum[from]
\tans, _ := strconv.Atoi(string(byteNum))
\treturn ans
}