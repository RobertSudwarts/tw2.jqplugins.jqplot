<%namespace name="tw" module="tw2.core.mako_util"/>
<div>
<div ${tw.attrs(attrs=w.attrs)}></div>
<script type="text/javascript">
$(document).ready(
    function(){
		doJQPlotWidget(
			'${w.selector}',
			//replace with jsonurl...
			${w._data},
			${w._options}
		);
    }
);
</script>
</div>
