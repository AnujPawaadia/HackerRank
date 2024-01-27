if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))

    # Remove duplicates and sort the scores in descending order
    unique_scores = sorted(set(scores), reverse=True)

    # The second element in the sorted list will be the runner-up score
    runner_up_score = unique_scores[1]

    print(runner_up_score)
