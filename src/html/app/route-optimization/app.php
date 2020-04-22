<div class="container maincontent">
  <div class="row">
    <div class="col-12 mb-3">
      <div><h1>Route Optimization</h1></div>
      <div>
        <p>Enter up to 10 destinations, one per line.</p>
        <p>It is assumed that (1) the first location is the origin and (2) you don't return back to the origin.</p>
        <form action="javascript:void(0);" method="post" id="route-opt-form">
          <textarea type="text" id="route-opt-input" placeholder="Destinations" required autofocus rows="10" cols="35"></textarea><br>
          <button type="submit">Submit</button>
        </form>
      </div>
      <hr/>
      <div>
        <p>The optimal route is:</p>
        <p id="optimal-route"></p>
      </div>
      <hr/>
      <div>
        <p>We use Google Distance Matrix API and Google Map JavaScript API with a customized optimization algorithm to calculate the fastest route.</p>
      </div>
      <hr/>
      <div>
        <p class="footnote mb-3">This project was done in collaboration with <a href="https://github.com/yiningwoof" target="_blank">Yining Wang</a>. We thank <a href="https://github.com/bgjehu" target="_blank">Jieyi "Jay" Hu</a> for his support and input.</p>
      </div>
    </div><!--column-->
  </div><!--row-->
</div><!--maincontent-->
