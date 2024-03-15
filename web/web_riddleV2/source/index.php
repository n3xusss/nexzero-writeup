<?php
error_reporting(0);

$black_list = [
    '127.0.0.1', 'localhost', '127.1', '127.0.1', '0.0.0.0', '127.0.1.3', '127.0.1.1', '::1', '[::]', '0', '[0000::1]'
];

$result = null;

$allowed_domains = ['nexus-security-club.com'];

if (isset($_GET['host']) && preg_match('/^http:\/\/nex-zero\.nexus-security-club\.com(:\d+)?\/.*/i', $_GET['host']) && strpos($_GET['host'], $allowed_domain) !== false) {
    $chor = curl_init();
    curl_setopt($chor, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($chor, CURLOPT_TIMEOUT, 7);
    curl_setopt($chor, CURLOPT_URL, $_GET['host']);
    $result = curl_exec($chor);

    if ($result === false) {
        $result = "timed out!";
    } else if (strpos($result, 'bGh3YSB5amliZWsgbGh3YSB5amliZWs=') !== false) {
        $result = "nexus{FAKE_FLAG_V2}";
    }
    curl_close($chor);
} else {
    $result = "Invalid URL or domain!";
}
?>

<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <title>WebRiddle</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/highlight.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/styles/default.min.css">
    <script>hljs.initHighlightingOnLoad()</script>
</head>
<body>
    <section class="bg-light">
        <div class="py-8 px-4 mx-auto">
            <div class="mx-auto text-center">
                <h2 class="mb-4 text-4xl font-extrabold text-dark">
                    WebRiddle
                </h2>

                <form action="" method="GET">
                    <div class="mb-6 mt-4">
                        <label for="default-input" class="form-label">Website URL</label>
                        <input type="text" id="default-input" name="host"
                            class="form-control" placeholder="http://allowed_domains/bla_bla">
                        <button class="btn btn-dark mb-3 mt-3">
                            Crawl
                        </button>
                    </div>
                </form>
                <div class="bg-light rounded-lg shadow-md border border-dark">
                    <h5 class="mb-2 text-2xl text-dark text-center">
                        crawled
                    </h5>
                    <hr class="my-2 h-px border-0 bg-dark">
                    <div class="rounded-lg overflow-hidden">
                        <pre class="font-normal text-dark">
                            <code class="language-html"><?php echo !empty($result) ? htmlspecialchars($result) : "No results"; ?></code>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>