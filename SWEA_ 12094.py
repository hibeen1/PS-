from itertools import product
import sys
from itertools import combinations 

input = sys.stdin.readline
INF = int(1e9)

t = int(input())
ans_list = []
for tc in range(t):
    dp = [INF for _ in range(1000)]
    n, o, m = map(int, input().split())
    combi = []
    possible_num = sorted(list(map(int, input().split())))
    combi.append(list(combinations(possible_num, 2)))
    print(combi)
    possible_oper = sorted(list(map(int, input().split())))
    ans_list.append("#" + str(tc+1) + " ")

# #include <iostream>
# using namespace std;
# int N, O, M;
# int nums[11];
# char opers[5];
# int targetNum;
# int best[1000];
# int used[1000];
# int johap[1000];
# int joCnt;
# int johapNumCnt[1000];
# int johapUsed[1000];
# void init()
# {
# 	for (int i = 0; i < 1000; i++) {
# 		best[i] = 99;
# 		used[i] = 0;
# 	}
# 	for (int i = 0; i < joCnt; i++) {
# 		int num = johap[i];
# 		best[num] = johapNumCnt[i];
# 	}
# }
# int getCalResult(int a, char oper, int b)
# {
# 	if (oper == '*') return a * b;
# 	if (oper == '-') return a - b;
# 	if (oper == '/') return a / b;
# 	return a + b;
# }
# void getMinTouchCnt(int touchCnt, int now)
# {
# 	for (int x = 0 ; x<O; x++) {
# 		for (int i = 0; i < joCnt; i++) {
# 			int num = johap[i];
# 			int nextCnt = touchCnt + johapNumCnt[i] + 1;
# 			if (nextCnt > M - 1) break;
# 			if (opers[x] == '/' && num == 0) continue;
# 			int next = getCalResult(now, opers[x], num);
			
# 			if (opers[x] == '+' && next > 999) break;
# 			if (opers[x] == '-' && next < 0) break;
# 			if (opers[x] == '*' && next > 999) break;
# 			if (used[next] == 1) continue;
# 			if (best[next] <= nextCnt) continue;
			
# 			best[next] = nextCnt;
# 			used[next] = 1;
# 			getMinTouchCnt(nextCnt, next);
# 			used[next] = 0;
# 		}
# 	}
# }
# void getJoHapDFS(int lev, int sum)
# {
# 	for (int i = 0; i < N; i++) {
# 		int next = sum * 10 + nums[i];
# 		if (next > 999) continue;
# 		if (johapUsed[next] == 1) continue;
# 		johapUsed[next] = 1;
# 		getJoHapDFS(lev + 1, next);
# 	}
# }
# void getJohap()
# {
# 	for (int i = 0; i < 1000; i++) {
# 		johap[i] = 0;
# 		johapUsed[i] = 0;
# 		johapNumCnt[i] = 0;
# 	}
# 	joCnt = 0;
# 	getJoHapDFS(0, 0);
# 	for (int i = 0; i < 1000; i++) {
# 		if (johapUsed[i] == 0) continue;
# 		johap[joCnt] = i;
# 		if (i < 10) johapNumCnt[joCnt] = 1;
# 		else if (i < 100) johapNumCnt[joCnt] = 2;
# 		else if (i < 1000) johapNumCnt[joCnt] = 3;
# 		joCnt++;
# 	}
# }
# int main()
# {
# 	//freopen("text.txt", "r", stdin);
	
# 	int tcCnt;
# 	cin >> tcCnt;
# 	for (int tc = 1; tc <= tcCnt; tc++) {
# 		cin >> N >> O >> M;
	
# 		for (int i = 0; i < N; i++) cin >> nums[i];
# 		for (int i = 0; i < O; i++) {
# 			int t;
# 			cin >> t;
# 			if (t == 1) opers[i] = '+';
# 			if (t == 2) opers[i] = '-';
# 			if (t == 3) opers[i] = '*';
# 			if (t == 4) opers[i] = '/';
# 		}
# 		cin >> targetNum;
# 		getJohap();
# 		init();
# 		int ret = 0;
# 		if (best[targetNum] != 99) ret = best[targetNum];
# 		else {
# 			for (int i = 0; i < joCnt; i++) {
# 				getMinTouchCnt(johapNumCnt[i], johap[i]);
# 			}
# 			ret = best[targetNum] + 1;
# 		}
		
# 		if (best[targetNum] == 99) ret = -1;
# 		cout << "#" << tc << " " << ret << "\n";
# 	}
# 	return 0;
# }


# © Color Scripter. All rights reserved.


