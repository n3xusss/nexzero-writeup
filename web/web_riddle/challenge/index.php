<?php
error_reporting(0);


$black_list = [
    '127.0.0.1','localhost','127.1','127.0.1','0.0.0.0','127.0.1.3','127.0.1.1','::1','[::]','0','[0000::1]'
    ];

$result = null;


if (isset($_GET['host']) && preg_match('/^(https?:\/\/)?([a-z0-9\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?(?:\?.*)?$/', $_GET['host'])) {
    $par_url = parse_url($_GET['host']);

    if (in_array($par_url['host'], $black_list)) {
        $result = "not that easy!";
    } else {
        $hostname = gethostbyname($par_url['host']);
        $chor = curl_init();
        curl_setopt($chor, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($chor, CURLOPT_TIMEOUT, 5);
        curl_setopt($chor, CURLOPT_URL, $_GET['host']);
        $result = curl_exec($chor);
        if ($result === false) {
            $result = "timed out!";
        } else if (strpos($result, 'bGh3YSB5ZGlrIGxod2EgeWppYmVr=') !== false) {
            $result = "nexus{SSrf_With_DNs_RebiNd1nG_15_am4z1NG}";
        }
        curl_close($chor);
        $varx = $_GET['varx'] ;

    }
} else {
    $result = "Give a URL first.";
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
                            class="form-control" placeholder="http://example.com">
                        <input type="text" name="varx" style="display: none;"
                             >
                        <button class="btn btn-dark mb-3 mt-3">
                            Crawl
                        </button>
                    </div>
                </form>
                <div class="bg-light rounded-lg shadow-md border border-dark">
                    
                    <p class="text-light"><?php echo $varx; ?></p>
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
