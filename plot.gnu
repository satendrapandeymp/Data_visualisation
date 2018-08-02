set size ratio -1


set grid ytics lc rgb "#bbbbbb" lw 1 lt 0
set grid xtics lc rgb "#bbbbbb" lw 1 lt 0

set xlabel "X in meters"
set ylabel "Y in meters"

set terminal x11 1 size 1910,1060 position 5,5

#
set title "Beed rod with time"

plot 'data2.txt' us 3:4 with lines t'', 'data2.txt' us 3:4:($3 * 0 + .1) with circle t'' ;
#;

pause .0311
reread
