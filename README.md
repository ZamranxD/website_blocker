# website_blocker
A simple python tool to get rid of the distracting websites during your working hours. Just execute this process in the background and forget about distractions!



<h2>Here's how to run this as a background process :</h2>
<h3><i>For Linux/Mac</i></h3>
<ol>
<li>You can do this using cron. Run "sudo apt-get install cron" if you dont have it installed already.</li>
<li>Open your terminal and type <i>sudo crontab -e</i>. You might be prompted to select an editor if you're using cron for the first time. So just select any that you're comfortable with.</li>
<li>Once you've opened cron with sudo privillages, add the following line at the end of the file.</li>
<li><i><strong>@reboot python3 /home/user/Desktop/websiteBlocker/website_blocker.py</strong></i> Please note that the absolute path
of your website_blocker.py file might be different so please change it accordingly.</li>
<li>Once you're done, just save it and exit. And that's it. Done!</li>
</ol>

<h3><i>For Windows</i></h3>
<ol>
    <li>
        Check out <a href="https://youtu.be/ucPgmZzoUJQ">this video</a> for the tutorial. 
    </li>
</ol>
