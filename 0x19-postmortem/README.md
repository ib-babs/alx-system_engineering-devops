<h1>Issue Summary:</h1>
<ul>
    <li>The outage started at 09:18pm, West Africa Standard Time and ended at 10:00am West Africa Standard Time </li>
    <li> <strong>The impact and the user experience were: </strong><br>
        <ul>
        <li>Content failed to load</li>
        <li>Connection between api and the server refused</li>
        <li>Content was loaded incorrectly</li>
        <li>Page delivery was poor</li>
        <li>About all the users were affected.</li>
        </ul>
    </li>
    <li><strong>Root Cause:</strong><br>The root cause of all these impacts was, The server api was also experiencing downtime and sometimes, the load was much on the server</li> 
</ul>

<h1>Timeline:</h1>
<ul>
<li><h3>When the issue was detected<h3>The issue was detected when the end user load the uri named which was attached mostly to the api used<i>/pictures</i></li>
<li><h3>How the issue was detected<h3>The end user made a report about the bug</li>
<li><h3>Action taken<h3>The api owner was contacted; Source code of the uri path '/picture' was refactored</li>
<li><h3>misleading investigation/debugging paths that were taken</h3> Most of the time to root out the issue was implemented on checking the source code of the application. Debugging the website with console. The part of the application source code was refractored. The refractoring led to breakages of handful of code.</li>
<li><h3>which team/individuals was the incident escalated to</h3> The website was developed by only one developer.</li>
<li><h3>how the incident was resolved</h3>he api owner was contacted with immediate alacrity. It was said that the load was much on the server and the technician had had it fixed. Some features were also added to the application to rectify the page delivery.</li>
</ul>
